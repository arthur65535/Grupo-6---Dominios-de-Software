import {useCallback} from 'react';

// Types
import {IButtonViewModel} from './types';

const useButtonViewModel = ({onPress, loading}: IButtonViewModel) => {
  const _handleOnPressFunction = useCallback(() => {
    if (!loading && onPress) {
      return onPress();
    }

    return undefined;
  }, [onPress, loading]);

  return {onPressButton: _handleOnPressFunction};
};

export default useButtonViewModel;
