import styled from 'styled-components/native';
import {colors, metrics} from '~/styles';

export const Container = styled.View<{
  marginTop?: number;
  marginBottom: number;
}>`
  flex-direction: row;
  border-radius: 200px;
  height: 35px;
  border-color: ${colors.grey1};
  border-width: 1px;
  width: 100%;
  margin-bottom: ${props =>
    props.marginBottom !== undefined ? props.marginBottom : 20}px;
  margin-top: ${props =>
    props.marginTop !== undefined ? props.marginTop : 35}px;
`;

export const Button = styled.TouchableOpacity<{
  background?: string;
  selected: boolean;
}>`
  flex: 1;
  align-items: center;
  justify-content: center;
  border-radius: 80px;
  background-color: ${props =>
    !props.selected ? colors.white : props.background || colors.secondary};
`;

export const ButtonText = styled.Text<{color?: string; selected: boolean}>`
  font-size: ${metrics.fontSizeLow}px;
  color: ${props =>
    !props.selected ? colors.black : props.color || colors.white};
`;
