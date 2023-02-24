import styled from 'styled-components/native';

// Colors
import {colors} from '~/styles';

import background from '~/assets/png/background.png';

export const Container = styled.View`
  flex: 1;
  background-color: ${colors.tertiary};
  align-items: center;
  justify-content: center;
`;

export const BackgrounImage = styled.Image.attrs({
  source: background,
  resizeMode: 'cover',
})`
  position: absolute;
  width: 100%;
  height: 100%;
`;

export const Content = styled.View`
  width: 100%;
  align-items: center;
  justify-content: center;
  padding: 20px;
`;
