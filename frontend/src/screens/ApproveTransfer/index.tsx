import React, {useRef, useState} from 'react';

// Libs
import {StackNavigationProp} from '@react-navigation/stack';
import {RouteProp, useNavigation, useRoute} from '@react-navigation/native';

// Components
import Icon from '~/components/Icon';
import BottomSheet from '~/components/BottomSheet';
import StepIndicator from '~/components/StepIndicator';
import HospitalItemList from '~/components/HospitalItemList';
import TransportItemList from '~/components/TransportItemList';
import Button from '~/components/Button';

// Types
import {RootStackParamList} from '~/routes/app.routes';
import {IHospital} from '~/types/hospital';
import {ITransport} from '~/types/transport';

// Styles
import {
  Container,
  PatientInfoContainer,
  ImageContainer,
  PatientName,
  PatientStatus,
  ScrollContainer,
  BottomSheetContainer,
  HospitalContainer,
  ConfirmationContainer,
  FlexButton,
  Text,
  TransportContainer,
  ButtonContainer,
} from './styles';
import {colors, statusColor} from '~/styles';

// Enums
import {TRANSFER_STATUS} from '~/enums/transfer.enum';

// Mocks
import patients from '~/mocks/patients';
import {hospitals} from '~/mocks/hospitals';
import transports from '~/mocks/transport';

const ApproveTransfer: React.FC = () => {
  const navigation =
    useNavigation<StackNavigationProp<RootStackParamList, 'Patient'>>();
  const route = useRoute<RouteProp<RootStackParamList, 'ApproveTransfer'>>();

  const [patient] = useState(
    patients.find(item => item.id === route.params.patientID),
  );

  const [selectedHospital, setSelectedHospital] = useState<
    IHospital | undefined
  >();
  const [selectedTransport, setSelectedTransport] = useState<
    ITransport | undefined
  >();

  const [currentStep, setCurrentStep] = useState(0);

  const bottomSheetSelectHospitalRef = useRef<any>(null);
  const bottomSheetSelectTransportRef = useRef<any>(null);

  const _renderSteps = () => {
    if (currentStep === 0) {
      return (
        <HospitalContainer>
          {selectedHospital === undefined && (
            <FlexButton
              onPress={() => bottomSheetSelectHospitalRef?.current?.expand()}>
              <Text>Clique para selecionar</Text>
            </FlexButton>
          )}
          {selectedHospital !== undefined && (
            <HospitalItemList
              {...selectedHospital}
              onPress={() => {
                bottomSheetSelectHospitalRef?.current?.expand();
              }}
            />
          )}
        </HospitalContainer>
      );
    } else if (currentStep === 1) {
      return (
        <TransportContainer>
          {selectedTransport === undefined && (
            <FlexButton
              onPress={() => bottomSheetSelectTransportRef?.current?.expand()}>
              <Text>Clique para selecionar</Text>
            </FlexButton>
          )}
          {selectedTransport !== undefined && (
            <TransportItemList
              {...selectedTransport}
              onPress={() => {
                bottomSheetSelectTransportRef?.current?.expand();
              }}
            />
          )}
        </TransportContainer>
      );
    }

    return (
      <ConfirmationContainer>
        {selectedTransport !== undefined && selectedHospital !== undefined && (
          <>
            <HospitalItemList
              {...selectedHospital}
              onPress={() => {
                bottomSheetSelectHospitalRef?.current?.expand();
              }}
            />

            <TransportItemList
              {...selectedTransport}
              onPress={() => {
                bottomSheetSelectTransportRef?.current?.expand();
              }}
            />

            <ButtonContainer>
              <Button
                title="Confirmar"
                onPress={() => navigation.navigate('Home')}
                // loading
              />
            </ButtonContainer>
          </>
        )}

        {selectedHospital === undefined && (
          <FlexButton
            onPress={() => bottomSheetSelectHospitalRef?.current?.expand()}>
            <Text>Selecione o destino</Text>
          </FlexButton>
        )}

        {selectedTransport === undefined && selectedHospital !== undefined && (
          <FlexButton
            onPress={() => bottomSheetSelectTransportRef?.current?.expand()}>
            <Text>Selecione o transporte</Text>
          </FlexButton>
        )}
      </ConfirmationContainer>
    );
  };

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

          <StepIndicator
            currentStep={currentStep}
            labels={['Hospital', 'Transporte', 'Confirmação']}
            setCurrentStep={setCurrentStep}
          />

          {_renderSteps()}
        </ScrollContainer>

        <BottomSheet
          title="Selecionar Hospital"
          ref={bottomSheetSelectHospitalRef}
          maxHeight="70%">
          <BottomSheetContainer>
            {hospitals.map((hospital, index) => (
              <HospitalItemList
                key={index}
                {...hospital}
                onPress={h => {
                  setSelectedHospital(h);
                  bottomSheetSelectHospitalRef?.current?.collapse();
                }}
              />
            ))}
          </BottomSheetContainer>
        </BottomSheet>

        <BottomSheet
          title="Selecionar Transporte"
          ref={bottomSheetSelectTransportRef}
          maxHeight="70%">
          <BottomSheetContainer>
            {transports.map((transport, index) => (
              <TransportItemList
                key={index}
                {...transport}
                onPress={t => {
                  setSelectedTransport(t);
                  bottomSheetSelectTransportRef?.current?.collapse();
                }}
              />
            ))}
          </BottomSheetContainer>
        </BottomSheet>
      </Container>
    );
  }

  return <></>;
};

export default ApproveTransfer;
