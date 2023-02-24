import styled from 'styled-components/native';

// Colors
import {colors} from '~/styles';

export const Container = styled.TouchableOpacity`
  width: 100%;
  padding: 10px;
`;

export const Name = styled.Text`
  color: ${colors.black};
  font-size: 18px;
  font-weight: bold;
  margin-bottom: 5px;
`;

export const Location = styled.Text`
  color: ${colors.black};
  font-size: 13px;
`;

export const Specialities = styled.Text<{bold?: boolean}>`
  margin-top: 5px;
  color: ${colors.black};
  font-size: 13px;
  font-weight: ${props => (props.bold ? 'bold' : 'normal')};
`;
