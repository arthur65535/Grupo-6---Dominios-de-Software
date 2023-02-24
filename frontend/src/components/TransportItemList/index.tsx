import React from 'react';

// Types
import {ITransport} from '~/types/transport';

// Styles
import {Container, Name} from './styles';

interface Props extends ITransport {
  onPress: (transport: ITransport) => void;
}

const TransportItemList: React.FC<Props> = ({id, name, onPress}) => {
  return (
    <Container
      onPress={() =>
        onPress({
          id,
          name,
        })
      }>
      <Name numberOfLines={1}>{name}</Name>
    </Container>
  );
};

export default TransportItemList;
