import styled from 'styled-components/native';

// Colors
import {colors} from '~/styles';

export const Container = styled.View`
  flex: 1;
  background-color: ${colors.white};
`;

export const PatientInfoContainer = styled.View`
  align-items: center;
  margin: 20px;
`;

export const BottomSheetContainer = styled.View`
  flex: 1;
  margin-top: 30px;
  padding: 0 10px;
`;

export const ImageContainer = styled.View<{background: string}>`
  background-color: ${props => props.background};
  width: 100px;
  height: 100px;
  border-radius: 100px;
  justify-content: center;
  align-items: center;
  margin-bottom: 10px;
`;

export const PatientName = styled.Text`
  color: ${colors.black};
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 5px;
`;

export const PatientStatus = styled.Text<{color: string}>`
  color: ${props => props.color};
  font-size: 16px;
  font-weight: bold;
`;
