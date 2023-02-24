import React from 'react';

// Libs
import {useNavigation} from '@react-navigation/native';
import {StackNavigationProp} from '@react-navigation/stack';

// Components
import InProgressRow from '~/components/InProgressRow';

// Styles
import {Container, ScrollContainer} from './styles';
import {statusColor} from '~/styles';

// Types
import {RootStackParamList} from '~/routes/app.routes';

// Enums
import {TRANSFER_STATUS, TRANSFER_TYPE} from '~/enums/transfer.enum';

// Mocks
import patients from '~/mocks/patients';

const InProgress: React.FC = () => {
  const navigation =
    useNavigation<StackNavigationProp<RootStackParamList, 'InProgress'>>();

  return (
    <Container>
      <ScrollContainer>
        {patients.map((patient, index) => {
          return (
            <InProgressRow
              key={index}
              name={patient.name}
              status={TRANSFER_STATUS[patient.status]}
              statusColor={statusColor[patient.status]}
              type={TRANSFER_TYPE[patient.transferType]}
              action={() =>
                navigation.navigate('Transfer', {patientID: patient.id})
              }
            />
          );
        })}
      </ScrollContainer>
    </Container>
  );
};
export default InProgress;
