import React from 'react';

// Components

// Styles
import {Container, Button, ButtonText} from './styles';

interface ITabButton {
  title: string;
  color?: string;
  background?: string;
  action?: () => void;
}

const TabButton: React.FC<{
  buttons: ITabButton[];
  selectedButton: number;
  marginTop?: number;
  marginBottom?: number;
}> = ({buttons = [], selectedButton = 0, marginTop, marginBottom}) => {
  return (
    <Container marginTop={marginTop} marginBottom={marginBottom}>
      {buttons.map((item: ITabButton, index: number) => {
        return (
          <Button
            key={index}
            onPress={item.action}
            backgroung={item.background}
            selected={selectedButton === index}>
            <ButtonText color={item.color} selected={selectedButton === index}>
              {item.title}
            </ButtonText>
          </Button>
        );
      })}
    </Container>
  );
};

export default TabButton;
