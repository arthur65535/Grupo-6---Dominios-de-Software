import styled from 'styled-components/native';

// Colors
import {colors} from '~/styles';

export const Container = styled.TouchableOpacity`
  flex-direction: row;
  align-items: center;
  width: 100%;
  padding: 5px 10px;
  margin-top: 10px;
`;

export const ImageContainer = styled.View<{background: string}>`
  background-color: ${props => props.background};
  width: 50px;
  height: 50px;
  border-radius: 100px;
  justify-content: center;
  align-items: center;
  margin-right: 15px;
`;

export const InfoContainer = styled.View`
  flex: 1;
`;

export const Title = styled.Text`
  color: ${colors.black};
  font-weight: bold;
`;

export const StatusText = styled.Text<{color: string}>`
  color: ${(props: {color: string}) => props.color};
  font-weight: bold;
`;

export const TransferencyType = styled.Text`
  color: ${colors.grey};
`;
