import React, {useEffect, useRef, useState} from 'react';

// Libs
import {RouteProp, useRoute} from '@react-navigation/native';
import MapView, {Marker, Polyline as Route} from 'react-native-maps';
import Polyline from '@mapbox/polyline';

// Components
import Icon from '~/components/Icon';
import BottomSheet from '~/components/BottomSheet';

// Types
import {RootStackParamList} from '~/routes/app.routes';

// Styles
import {
  Container,
  PatientInfoContainer,
  ImageContainer,
  PatientName,
  PatientStatus,
  BottomSheetContainer,
} from './styles';
import {colors, statusColor} from '~/styles';

// Images
import Ambulance from '~/assets/svg/ambulance.svg';

// Enums
import {TRANSFER_STATUS} from '~/enums/transfer.enum';

// Mocks
import patients from '~/mocks/patients';
import {StyleSheet, View} from 'react-native';

const Transfer: React.FC = () => {
  const route = useRoute<RouteProp<RootStackParamList, 'Transfer'>>();

  const [patient] = useState(
    patients.find(item => item.id === route.params.patientID),
  );

  const bottomSheetPatientStatusRef = useRef<any>(null);
  const mapRef = useRef<MapView | null>(null);

  const getMapRoute = () => {
    const points = Polyline.decode(
      'dfxdBnqqkHq@NIDENuCn@cATECIESEIAIBGFAHg@YGEa@WgFyCIIKSScAlH_BEYg@eC',
    );

    const coords = points.map(point => ({
      latitude: point[0],
      longitude: point[1],
    }));

    return coords;
  };

  useEffect(() => {
    mapRef?.current?.fitToCoordinates(getMapRoute(), {
      edgePadding: {top: 50, right: 50, bottom: 50, left: 50},
      animated: true,
    });
  }, []);

  if (patient) {
    return (
      <Container>
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

        <MapView style={styles.map} ref={mapRef}>
          <Route
            coordinates={getMapRoute()}
            strokeWidth={3}
            strokeColor={colors.secondary}
          />

          <Marker
            coordinate={getMapRoute()[0]}
            title={'Hospital de cancer Araújo Jorge'}
            description={'Unidade de origem'}
          />

          <Marker
            coordinate={getMapRoute()[22]}
            title={'Hospital das Clínicas - UFG'}
            description={'Unidade de destino'}
          />

          <Marker coordinate={getMapRoute()[4]} title={'Ambulância 01'} flat>
            <View>
              <Ambulance width={30} height={30} />
            </View>
          </Marker>
        </MapView>

        <BottomSheet
          title="Editar Status"
          ref={bottomSheetPatientStatusRef}
          maxHeight="70%">
          <BottomSheetContainer>
            <></>
          </BottomSheetContainer>
        </BottomSheet>
      </Container>
    );
  }

  return <></>;
};

const styles = StyleSheet.create({
  map: {flex: 1},
});

export default Transfer;
