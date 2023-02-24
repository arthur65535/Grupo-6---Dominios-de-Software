import React, {useImperativeHandle} from 'react';
import {Animated, StyleSheet, TouchableOpacity} from 'react-native';

// Libs
import ReanimatedBottomSheet from 'reanimated-bottom-sheet';

// Styles
import {
  BottomSheetContent,
  CloseIcon,
  HeaderActionButton,
  HeaderContainer,
  Title,
} from './styles';

// View Model
import useBottomSheet from './view.model';

interface IBottomSheetHandle {
  expand(): void;
  collapse(): void;
}

interface IBottomSheet {
  title?: string;
  children: JSX.Element;
  maxHeight?: number | string;
  onClose?: () => void;
  onOpen?: () => void;
}

const BottomSheet = React.forwardRef<IBottomSheetHandle, IBottomSheet>(
  (
    {
      title = '',
      children = <></>,
      maxHeight = '90%',
      onClose = () => {},
      onOpen = () => {},
    },
    ref,
  ) => {
    const {bottomSheetRef, expand, collapse, isOpen, window} = useBottomSheet({
      onClose,
      onOpen,
    });

    const styles = StyleSheet.create({
      animatedView: {
        opacity: 0.7,
        backgroundColor: '#000000',
        position: 'absolute',
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        zIndex: 1,
      },

      animatedViewButton: {
        width: window.width,
        height: window.height,
        backgroundColor: 'transparent',
      },
    });

    useImperativeHandle(ref, () => ({
      expand: () => expand(),
      collapse: () => collapse(),
    }));

    return (
      <>
        {isOpen && (
          <Animated.View style={styles.animatedView}>
            <TouchableOpacity
              style={styles.animatedViewButton}
              activeOpacity={1}
              onPress={collapse}
            />
          </Animated.View>
        )}
        <ReanimatedBottomSheet
          ref={bottomSheetRef}
          snapPoints={[maxHeight, 0]}
          initialSnap={1}
          enabledContentGestureInteraction={false}
          renderHeader={() => (
            <HeaderContainer>
              <HeaderActionButton onPress={collapse}>
                <CloseIcon />
              </HeaderActionButton>
              <Title>{title}</Title>
              <HeaderActionButton />
            </HeaderContainer>
          )}
          renderContent={() => (
            <BottomSheetContent>{children}</BottomSheetContent>
          )}
          onCloseEnd={collapse}
        />
      </>
    );
  },
);

export default BottomSheet;
