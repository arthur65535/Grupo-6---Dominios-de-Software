import React from 'react';

// Libs
import {useNavigation} from '@react-navigation/native';
import {StackNavigationProp} from '@react-navigation/stack';

// Components
import HomeRow from '~/components/HomeRow';

// Types
import {RootStackParamList} from '~/routes/app.routes';

// Styles
import {
  Container,
  ConnectionStatusContainer,
  ConnectionStatus,
  ConnectionStatusText,
  ScrollContainer,
} from './styles';
import {statusColor} from '~/styles';

// Enums
import {TRANSFER_STATUS, TRANSFER_TYPE} from '~/enums/transfer.enum';

// Mocks
import patients from '~/mocks/patients';

const Home: React.FC = () => {
  const navigation =
    useNavigation<StackNavigationProp<RootStackParamList, 'Home'>>();

  return (
    <Container>
      <ConnectionStatusContainer>
        <ConnectionStatus />
        <ConnectionStatusText>Você está conectado</ConnectionStatusText>
      </ConnectionStatusContainer>

      <ScrollContainer>
        {patients.map((patient, index) => {
          return (
            <HomeRow
              key={index}
              name={patient.name}
              status={TRANSFER_STATUS[patient.status]}
              statusColor={statusColor[patient.status]}
              type={TRANSFER_TYPE[patient.transferType]}
              action={() =>
                navigation.navigate('Patient', {patientID: patient.id})
              }
            />
          );
        })}
      </ScrollContainer>
    </Container>
  );
};

export default Home;
