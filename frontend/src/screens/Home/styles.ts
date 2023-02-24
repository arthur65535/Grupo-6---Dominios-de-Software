import styled from 'styled-components/native';

// Colors
import {colors} from '~/styles';

export const Container = styled.View`
  flex: 1;
  background-color: ${colors.white};
`;

export const ConnectionStatusContainer = styled.View`
  background-color: ${colors.ice};
  padding: 10px;
  width: 100%;
  flex-direction: row;
  align-items: center;
`;

export const ConnectionStatus = styled.View`
  background-color: ${colors.success};
  width: 10px;
  height: 10px;
  border-radius: 100px;
  margin-right: 10px;
`;

export const ConnectionStatusText = styled.Text`
  color: ${colors.black};
  font-weight: bold;
`;

export const ScrollContainer = styled.ScrollView``;
