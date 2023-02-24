import React from 'react';
import {colors} from '~/styles';
import Icon from '../Icon';

// Styles
import {
  Container,
  ImageContainer,
  InfoContainer,
  StatusText,
  Title,
  TransferencyType,
} from './styles';

interface IHomeRow {
  name: string;
  statusColor: string;
  status: string;
  type: string;
  action?: () => void;
}

const HomeRow: React.FC<IHomeRow> = ({
  name,
  statusColor,
  status,
  type,
  action,
}) => {
  return (
    <Container onPress={action}>
      <ImageContainer background={statusColor}>
        <Icon name="account" color={colors.white} />
      </ImageContainer>
      <InfoContainer>
        <Title>{name}</Title>
        <StatusText color={statusColor}>{status}</StatusText>
        <TransferencyType>{type}</TransferencyType>
      </InfoContainer>
    </Container>
  );
};

export default HomeRow;
