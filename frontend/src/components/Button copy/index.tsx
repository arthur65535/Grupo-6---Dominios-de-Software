import React, {useCallback} from 'react';

// Styles
import {Container, Text, Loading} from './styles';

// View Model
import useButtonViewModel from './viewModel';

// Types
import {IButton} from './types';

const Button: React.FC<IButton> = ({
  title,
  onPress,
  loading,
  background,
  color,
  ...rest
}) => {
  const {onPressButton} = useButtonViewModel({loading, onPress});

  const renderButtonContent = useCallback(() => {
    if (loading) {
      return <Loading />;
    }

    return (
      <Text color={color} disabled={rest.disabled}>
        {title}
      </Text>
    );
  }, [loading, color, rest.disabled, title]);

  return (
    <Container
      background={background}
      onPress={onPressButton}
      disabled={rest.disabled}
      {...rest}>
      {renderButtonContent()}
    </Container>
  );
};

export default Button;
