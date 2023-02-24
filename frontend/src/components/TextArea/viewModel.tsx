import {useCallback, useEffect, useMemo, useRef} from 'react';
import {Animated} from 'react-native';
import {colors} from '~/styles';
import {hexToRgb} from '~/utils/colorTransform';

// Types
import {ITextAreaViewModel} from './types';

const useTextAreaViewModel = ({value}: ITextAreaViewModel) => {
  const placeHolderAnimateSliding = useRef(new Animated.Value(0));
  const placeHolderAnimateZoom = useRef(new Animated.Value(16));
  const placeHolderAnimateColor = useRef(new Animated.Value(0));

  const animatePlaceHolderStart = useCallback(() => {
    Animated.timing(placeHolderAnimateSliding.current, {
      toValue: -17,
      duration: 300,
      useNativeDriver: false,
    }).start();

    Animated.timing(placeHolderAnimateZoom.current, {
      toValue: 12,
      duration: 300,
      useNativeDriver: false,
    }).start();

    Animated.timing(placeHolderAnimateColor.current, {
      toValue: 1,
      duration: 300,
      useNativeDriver: false,
    }).start();
  }, []);

  const animatePlaceHolderBlur = useCallback(() => {
    if (!value) {
      Animated.timing(placeHolderAnimateSliding.current, {
        toValue: 0,
        duration: 300,
        useNativeDriver: false,
      }).start();

      Animated.timing(placeHolderAnimateZoom.current, {
        toValue: 16,
        duration: 300,
        useNativeDriver: false,
      }).start();

      Animated.timing(placeHolderAnimateColor.current, {
        toValue: 0,
        duration: 300,
        useNativeDriver: false,
      }).start();
    }
  }, [value]);

  const placeHolderColor = useMemo(
    () =>
      placeHolderAnimateColor.current.interpolate({
        inputRange: [0, 1],
        outputRange: [hexToRgb(colors.black), hexToRgb(colors.black)],
      }),
    [],
  );

  useEffect(() => {
    if (value) {
      animatePlaceHolderStart();
    } else {
      animatePlaceHolderBlur();
    }
  }, [value, animatePlaceHolderStart, animatePlaceHolderBlur]);

  return {
    placeholderSlidingValue: placeHolderAnimateSliding.current,
    placeholderZoomValue: placeHolderAnimateZoom.current,
    placeholderColorValue: placeHolderColor,
  };
};

export default useTextAreaViewModel;
