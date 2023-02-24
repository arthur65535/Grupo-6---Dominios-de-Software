import styled from 'styled-components/native';
import MaskInput from 'react-native-mask-input';
import {colors} from '~/styles';

export const Container = styled.View`
  height: 55px;
  width: 100%;
  /* background-color: red; */
  margin-bottom: 5px;
`;

export const InputContent = styled.View`
  flex: 1;
  border-color: ${colors.white};
  border-bottom-width: 2px;
  justify-content: flex-end;
`;

export const Input = styled.TextInput.attrs({
  textAlignVertical: 'bottom',
})`
  font-size: 16px;
  color: ${colors.white};
  padding: 0;
`;

export const InputWithMask = styled(MaskInput)`
  font-size: 16px;
  color: ${colors.white};
  padding: 0;
`;

export const ErrorMessage = styled.Text`
  margin-top: 2px;
  font-size: 14px;
  color: ${colors.danger};
  font-weight: bold;
`;
