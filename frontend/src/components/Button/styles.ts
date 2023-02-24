import styled from 'styled-components/native';
import {colors} from '~/styles';

interface IContainer {
  background: string;
  disabled: boolean;
}

interface IText {
  color?: string;
  disabled: boolean;
}

const renderContainerBackground = ({background, disabled}: IContainer) => {
  if (disabled) {
    return `${background}55`;
  }

  return background;
};

const renderTextColor = ({color, disabled}: IText) => {
  if (disabled) {
    return `${color}44`;
  }

  return color;
};

export const Container = styled.TouchableOpacity<IContainer>`
  width: 100%;
  height: 45px;
  align-items: center;
  justify-content: center;
  background-color: ${props =>
    renderContainerBackground({
      background: props.background ?? colors.secondary,
      disabled: props.disabled,
    })};
  border-radius: 10px;
  margin-top: 20px;
`;

export const Text = styled.Text<IText>`
  font-size: 14px;
  font-weight: bold;
  color: ${props =>
    renderTextColor({
      color: props.color ?? colors.white,
      disabled: props.disabled,
    })};
`;

export const Loading = styled.ActivityIndicator.attrs({
  color: colors.white,
})``;
