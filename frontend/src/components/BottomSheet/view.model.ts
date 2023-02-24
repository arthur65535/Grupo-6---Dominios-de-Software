import {useCallback, useRef, useState} from 'react';
import {Animated, BackHandler, Dimensions, Keyboard} from 'react-native';

const useBottomSheet = ({
  onClose,
  onOpen,
}: {
  onClose: () => void;
  onOpen: () => void;
}) => {
  const window = Dimensions.get('screen');

  const bottomSheetRef = useRef<any>(null);

  const [isOpen, setIsOpen] = useState<boolean>(false);

  const backHandler = useRef<any>(null);

  const collapse = useCallback(() => {
    setIsOpen(false);

    Animated.timing(new Animated.Value(0), {
      toValue: 0,
      duration: 350,
      useNativeDriver: true,
    }).start();

    bottomSheetRef.current.snapTo(1);

    backHandler?.current?.remove();

    onClose();
  }, [onClose]);

  const backgroundAction = useCallback(() => {
    collapse();
    return true;
  }, [collapse]);

  const expand = useCallback(() => {
    setIsOpen(true);

    Keyboard.dismiss();

    backHandler.current = BackHandler.addEventListener(
      'hardwareBackPress',
      backgroundAction,
    );

    bottomSheetRef.current.snapTo(0);

    Animated.timing(new Animated.Value(0), {
      toValue: 0.7,
      duration: 300,
      useNativeDriver: true,
    }).start();

    onOpen();
  }, [onOpen, backgroundAction]);

  return {bottomSheetRef, expand, collapse, isOpen, window};
};

export default useBottomSheet;
