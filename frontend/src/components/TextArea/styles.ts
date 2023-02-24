import styled from 'styled-components/native';
import {colors} from '~/styles';

export const Container = styled.View`
  flex: 1;
  /* background-color: red; */
`;

export const InputContent = styled.View`
  flex: 1;
  justify-content: flex-start;
`;

export const Input = styled.TextInput.attrs({
  textAlignVertical: 'top',
})`
  font-size: 16px;
  color: ${colors.black};
  padding: 0;
`;

export const ErrorMessage = styled.Text`
  margin-top: 2px;
  font-size: 14px;
  color: ${colors.danger};
  font-weight: bold;
`;
