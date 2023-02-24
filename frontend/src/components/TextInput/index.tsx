import React, {useCallback} from 'react';
import {Animated, StyleSheet} from 'react-native';

// Styles
import {
  Container,
  InputContent,
  Input,
  InputWithMask,
  ErrorMessage,
} from './styles';

// View Model
import useTextInputViewModel from './viewModel';

// Types
import {ITextInput} from './types';

const TextInput: React.FC<ITextInput> = ({
  value,
  onChangeText,
  placeholder,
  mask,
  errorMessage,
  ...rest
}) => {
  const {placeholderSlidingValue, placeholderZoomValue, placeholderColorValue} =
    useTextInputViewModel({value});

  const renderInput = useCallback(() => {
    if (mask) {
      return (
        <InputWithMask
          value={value}
          onChangeText={onChangeText}
          placeholderTextColor="#ffffff00"
          mask={mask}
          {...rest}
        />
      );
    }

    return <Input value={value} onChangeText={onChangeText} {...rest} />;
  }, [mask, onChangeText, rest, value]);

  return (
    <Container>
      <InputContent>
        <Animated.Text
          style={[
            styles.placeHolderStyle,
            {
              fontSize: placeholderZoomValue,
              color: placeholderColorValue,
              transform: [
                {
                  translateY: placeholderSlidingValue,
                },
              ],
            },
          ]}>
          {placeholder}
        </Animated.Text>
        {renderInput()}
      </InputContent>
      <ErrorMessage>{errorMessage}</ErrorMessage>
    </Container>
  );
};

const styles = StyleSheet.create({
  placeHolderStyle: {
    position: 'absolute',
  },
});

export default TextInput;
