import React from 'react';

// Types
import {IHospital} from '~/types/hospital';

// Styles
import {Container, Location, Name, Specialities} from './styles';

// Mocks
import {
  specialities as specialistiesEnum,
  hospitalizations as hospitalizationsEnum,
} from '~/enums/hospital.enum';

interface Props extends IHospital {
  onPress: (hospital: IHospital) => void;
}

const HospitalItemList: React.FC<Props> = ({
  name,
  city,
  state,
  country,
  phone,
  specialities,
  hospitalizations,
  geolocation,
  onPress,
}) => {
  return (
    <Container
      onPress={() =>
        onPress({
          name,
          city,
          state,
          country,
          phone,
          specialities,
          hospitalizations,
          geolocation,
        })
      }>
      <Name numberOfLines={1}>{name}</Name>
      <Location>{`${city}, ${
        state ? `${state}, ` : ''
      }${country} | ${phone}`}</Location>

      <Specialities>
        <Specialities bold>{'Especialidades: '}</Specialities>
        {specialities?.map((specialityID, index) => {
          const speciality = specialistiesEnum.find(
            value => value.id === specialityID,
          )?.name;
          if (index === specialities.length - 1) {
            return speciality;
          } else {
            return `${speciality} | `;
          }
        })}
      </Specialities>

      <Specialities>
        <Specialities bold>{'Internações: '}</Specialities>

        {hospitalizations?.map((hospitalizationID, index) => {
          const hospitalization = hospitalizationsEnum.find(
            value => value.id === hospitalizationID,
          )?.name;
          if (index === hospitalizations.length - 1) {
            return hospitalization;
          } else {
            return `${hospitalization} | `;
          }
        })}
      </Specialities>
    </Container>
  );
};

export default HospitalItemList;
