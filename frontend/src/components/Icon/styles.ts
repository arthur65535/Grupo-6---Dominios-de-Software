import styled from 'styled-components/native';
import MaterialCommunityIcons from 'react-native-vector-icons/MaterialCommunityIcons';
import {colors} from '~/styles';

export const MaterialCommunityIconsStyle = styled(MaterialCommunityIcons).attrs(
  (props: {name: string; color: string; size: number | string}) => {
    return {
      name: props.name,
      color: props.color ? props.color : colors.white,
      size: props.size ? props.size : 20,
    };
  },
)``;
