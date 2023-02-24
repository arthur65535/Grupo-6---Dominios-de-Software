import React, {useCallback, useRef, useState} from 'react';
import {Alert} from 'react-native';

// Libs
import {RouteProp, useNavigation, useRoute} from '@react-navigation/native';

// Components
import Icon from '~/components/Icon';
import BottomSheet from '~/components/BottomSheet';
import TextArea from '~/components/TextArea';

// Types
import {RootStackParamList} from '~/routes/app.routes';
import {StackNavigationProp} from '@react-navigation/stack';

// Styles
import {
  Container,
  PatientInfoContainer,
  ImageContainer,
  PatientName,
  PatientStatus,
  ActionsContainer,
  ActionButton,
  ActionButtonText,
  PatientInfo,
  ScrollContainer,
  BottomSheetContainer,
  StatusListItem,
  StatusText,
} from './styles';
import {colors, statusColor} from '~/styles';

// Enums
import {TRANSFER_STATUS} from '~/enums/transfer.enum';

// Mocks
import patients from '~/mocks/patients';

const Patient: React.FC = () => {
  const navigation =
    useNavigation<StackNavigationProp<RootStackParamList, 'Patient'>>();
  const route = useRoute<RouteProp<RootStackParamList, 'Patient'>>();

  const [patient, setPatient] = useState(
    patients.find(item => item.id === route.params.patientID),
  );
  const [patientInfoText, setPatientInfoText] = useState(patient?.info || '');

  const bottomSheetPatientInfoRef = useRef<any>(null);
  const bottomSheetPatientStatusRef = useRef<any>(null);

  const _renderStatusItem = useCallback(() => {
    const statusList = Object.keys(TRANSFER_STATUS).map(value => {
      const customKey = value as keyof typeof TRANSFER_STATUS;
      return customKey;
    });

    return statusList.map((value, index) => {
      const color = statusColor[value];
      const text = TRANSFER_STATUS[value];

      return (
        <StatusListItem
          key={index}
          onPress={() => {
            if (patient) {
              setPatient({...patient, status: value});
              bottomSheetPatientStatusRef?.current?.collapse();
            } else {
              Alert.alert('Erro', 'Erro ao buscar paciente');
            }
          }}>
          <StatusText color={color}>{text}</StatusText>
        </StatusListItem>
      );
    });
  }, [patient]);

  if (patient) {
    return (
      <Container>
        <ScrollContainer>
          <PatientInfoContainer>
            <ImageContainer
              background={statusColor[patient.status ?? 'notUrgent']}>
              <Icon name="account" color={colors.white} size={60} />
            </ImageContainer>

            <PatientName>{patient.name}</PatientName>

            <PatientStatus color={statusColor[patient.status]}>
              {TRANSFER_STATUS[patient.status]}
            </PatientStatus>
          </PatientInfoContainer>

          <ActionsContainer>
            <ActionButton
              onPress={() => {
                if (patient.medicalRecordURL) {
                  navigation.navigate('PDF', {
                    uri: patient.medicalRecordURL,
                    patientName: patient.name,
                  });
                } else {
                  Alert.alert('Erro', 'Paciente sem dados no prontuário');
                }
              }}>
              <Icon name="file" color={colors.white} size={20} />
              <ActionButtonText>Prontuário</ActionButtonText>
            </ActionButton>

            <ActionButton
              onPress={() => bottomSheetPatientInfoRef?.current?.expand()}>
              <Icon name="pencil" color={colors.white} size={20} />
              <ActionButtonText>observações</ActionButtonText>
            </ActionButton>

            <ActionButton
              onPress={() => bottomSheetPatientStatusRef?.current?.expand()}>
              <Icon name="priority-high" color={colors.white} size={20} />
              <ActionButtonText>Status</ActionButtonText>
            </ActionButton>

            <ActionButton
              onPress={() =>
                navigation.navigate('ApproveTransfer', {patientID: patient.id})
              }>
              <Icon name="ambulance" color={colors.white} size={20} />
              <ActionButtonText>Transferir</ActionButtonText>
            </ActionButton>
          </ActionsContainer>

          <PatientInfo>{patientInfoText}</PatientInfo>
        </ScrollContainer>

        <BottomSheet
          title="Editar Observações"
          ref={bottomSheetPatientInfoRef}
          maxHeight="70%">
          <BottomSheetContainer>
            <TextArea
              placeholder="Informações do paciente"
              value={patientInfoText}
              onChangeText={value => setPatientInfoText(value)}
            />
          </BottomSheetContainer>
        </BottomSheet>

        <BottomSheet
          title="Editar Status"
          ref={bottomSheetPatientStatusRef}
          maxHeight="70%">
          <BottomSheetContainer>{_renderStatusItem()}</BottomSheetContainer>
        </BottomSheet>
      </Container>
    );
  }

  return <></>;
};

export default Patient;
