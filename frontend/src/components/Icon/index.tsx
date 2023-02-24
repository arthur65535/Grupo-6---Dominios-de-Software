import React, {FC} from 'react';
import {MaterialCommunityIconsStyle} from './styles';
import {colors} from '~/styles';
import {SvgProps} from 'react-native-svg';

const Icon: React.FC<{
  classItem?: 'Ionicons' | undefined;
  name?: string | undefined;
  color?: string | undefined;
  size?: number | undefined;
  SVG?: FC<SvgProps>;
}> = ({
  classItem = 'Ionicons',
  name = 'arrow-left',
  color = colors.secondary,
  size = 30,
  SVG = undefined,
}) => {
  if (SVG) {
    return <SVG width={size} height={size} />;
  } else if (name) {
    if (classItem === 'Ionicons') {
      return (
        <MaterialCommunityIconsStyle name={name} size={size} color={color} />
      );
    }

    return <></>;
  }

  return <></>;
};

export default Icon;
