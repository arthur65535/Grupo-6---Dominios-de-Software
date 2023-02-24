import React, {useCallback} from 'react';
import {Animated, StyleSheet} from 'react-native';

// Styles
import {Container, InputContent, Input, ErrorMessage} from './styles';

// View Model
import useTextAreaViewModel from './viewModel';

// Types
import {ITextArea} from './types';

const TextArea: React.FC<ITextArea> = ({
  value,
  onChangeText,
  placeholder,
  errorMessage,
  ...rest
}) => {
  const {placeholderSlidingValue, placeholderZoomValue, placeholderColorValue} =
    useTextAreaViewModel({value});

  const renderInput = useCallback(() => {
    return (
      <Input
        value={value}
        onChangeText={onChangeText}
        {...rest}
        multiline
        numberOfLines={10}
      />
    );
  }, [onChangeText, rest, value]);

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

export default TextArea;
