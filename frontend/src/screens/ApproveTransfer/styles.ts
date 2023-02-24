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

export const BottomSheetContainer = styled.ScrollView.attrs({
  contentContainerStyle: {
    paddingBottom: 50,
  },
})`
  flex: 1;
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

export const HospitalContainer = styled.View`
  flex: 1;
  padding-top: 30px;
`;

export const TransportContainer = styled.View`
  flex: 1;
  padding-top: 30px;
`;

export const ConfirmationContainer = styled.View`
  flex: 1;
`;

export const PatientStatus = styled.Text<{color: string}>`
  color: ${props => props.color};
  font-size: 16px;
  font-weight: bold;
`;

export const FlexButton = styled.TouchableOpacity`
  flex: 1;
  align-items: center;
  justify-content: center;
`;

export const Text = styled.Text``;

export const ScrollContainer = styled.ScrollView.attrs(() => ({
  contentContainerStyle: {
    flex: 1,
    flexGrow: 1,
  },
}))``;

export const ButtonContainer = styled.View`
  width: 100%;
  padding: 20px;
`;
