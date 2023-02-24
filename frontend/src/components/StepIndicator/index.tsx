import React from 'react';

// Libs
import RNStepIndicator from 'react-native-step-indicator';

// Colors
import {colors} from '~/styles';

interface IStepIndicator {
  currentStep: number;
  setCurrentStep: (index: number) => void;
  labels: string[];
}

const StepIndicator: React.FC<IStepIndicator> = ({
  currentStep,
  setCurrentStep,
  labels,
}) => {
  return (
    <RNStepIndicator
      currentPosition={currentStep}
      labels={labels}
      stepCount={labels.length}
      onPress={index => setCurrentStep(index)}
      customStyles={customStyles}
    />
  );
};

const customStyles = {
  stepIndicatorSize: 25,
  currentStepIndicatorSize: 30,
  separatorStrokeWidth: 2,
  currentStepStrokeWidth: 3,
  stepStrokeCurrentColor: colors.primary,
  stepStrokeWidth: 3,
  stepStrokeFinishedColor: colors.primary,
  stepStrokeUnFinishedColor: colors.ice,
  separatorFinishedColor: colors.primary,
  separatorUnFinishedColor: colors.ice,
  stepIndicatorFinishedColor: colors.primary,
  stepIndicatorUnFinishedColor: colors.white,
  stepIndicatorCurrentColor: colors.white,
  stepIndicatorLabelFontSize: 13,
  currentStepIndicatorLabelFontSize: 13,
  stepIndicatorLabelCurrentColor: colors.primary,
  stepIndicatorLabelFinishedColor: colors.white,
  stepIndicatorLabelUnFinishedColor: colors.ice,
  labelColor: colors.ice,
  labelSize: 13,
  currentStepLabelColor: colors.primary,
};

export default StepIndicator;
