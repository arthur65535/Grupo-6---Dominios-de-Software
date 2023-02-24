import styled from 'styled-components/native';

// Components
import Icon from '~/components/Icon';

// Colors
import {colors} from '~/styles';

export const BottomSheetContent = styled.View`
  background-color: ${colors.white};
  width: 100%;
  height: 100%;
`;

export const HeaderContainer = styled.View`
  background-color: ${colors.white};
  width: 100%;
  padding: 20px;
  align-items: center;
  border-top-left-radius: 20px;
  border-top-right-radius: 20px;
  flex-direction: row;
`;

export const HeaderActionButton = styled.TouchableOpacity`
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
`;

export const CloseIcon = styled(Icon).attrs(() => ({
  name: 'close',
  size: 22,
  color: colors.black,
}))``;

export const Title = styled.Text`
  flex: 1;
  text-align: center;
  font-weight: bold;
`;
