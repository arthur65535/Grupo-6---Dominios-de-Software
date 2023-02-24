import styled from 'styled-components/native';

// Colors
import {colors} from '~/styles';

export const Container = styled.View`
  flex: 1;
  background-color: ${colors.white};
`;

export const ScrollContainer = styled.ScrollView``;

export const PatientInfoContainer = styled.View`
  flex: 1;
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

export const ActionsContainer = styled.View`
  margin: 10px 0;
  flex-direction: row;
  justify-content: space-around;
`;

export const ActionButton = styled.TouchableOpacity`
  width: 70px;
  height: 70px;
  border-radius: 7px;
  background-color: ${colors.primary};
  align-items: center;
  justify-content: center;
`;

export const ActionButtonText = styled.Text`
  color: ${colors.white};
  font-size: 10px;
  margin-top: 5px;
`;

export const PatientInfo = styled.Text`
  color: ${colors.black};
  font-size: 14px;
  margin-top: 5px;
  text-align: justify;
  margin: 10px;
  margin-bottom: 40px;
`;

export const StatusListItem = styled.TouchableOpacity`
  border-bottom-width: 0.5px;
  border-color: ${colors.ice};
  height: 60px;
  justify-content: center;
`;

export const StatusText = styled.Text<{color: string}>`
  color: ${props => props.color};
  font-size: 16px;
  font-weight: bold;
`;
