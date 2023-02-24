import * as React from 'react';
import {
  ImageBackground,
  SafeAreaView,
  StyleSheet,
  TouchableHighlight,
  View,
} from 'react-native';

// Libs
import {NavigationContainer, StackActions} from '@react-navigation/native';
import {createStackNavigator} from '@react-navigation/stack';
import {
  BottomTabBarProps,
  createBottomTabNavigator,
} from '@react-navigation/bottom-tabs';

// Store

// Components
import Icon from '~/components/Icon';

// Styles
import {colors} from '~/styles';
import {Text} from 'react-native';

// Images
import HomeIcon from '~/assets/svg/home-icon.svg';
import menuBackground from '~/assets/png/menu-background.png';

// Screens
import Home from '~/screens/Home';
import Patient from '~/screens/Patient';
import PDF from '~/screens/PDF';
import ApproveTransfer from '~/screens/ApproveTransfer';
import Done from '~/screens/Done';
import InProgress from '~/screens/InProgress';
import Transfer from '~/screens/Transfer';

export type RootStackParamList = {
  Home: undefined;
  Done: undefined;
  Template: undefined;
  Patient: {patientID: number};
  PDF: {uri: string; patientName: string};
  ApproveTransfer: {patientID: number};
  InProgress: undefined;
  Transfer: {patientID: number};
};

const Tab = createBottomTabNavigator();
const Stack = createStackNavigator<RootStackParamList>();

const CustomTabButton = ({
  onPress,
  absolute,
  children,
}: {
  onPress?: () => void;
  absolute?: boolean;
  children: React.ReactNode;
}) => {
  return (
    <TouchableHighlight
      activeOpacity={1}
      underlayColor="#00000000"
      onPress={onPress}
      // eslint-disable-next-line react-native/no-inline-styles
      style={[styles.customTabButtonButton, {top: absolute ? -15 : 14}]}>
      <View style={styles.customTabButtonContainer}>{children}</View>
    </TouchableHighlight>
  );
};

function HomeRoutes() {
  return (
    <Stack.Navigator
      screenOptions={() => ({
        headerShown: false,
      })}>
      <Stack.Screen
        name="Home"
        component={Home}
        options={{
          title: 'Transferências solicitadas',
          headerShown: true,
          headerStyle: {
            backgroundColor: colors.primary,
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      />

      <Stack.Screen
        name="Patient"
        component={Patient}
        options={{
          title: 'Paciente',
          headerShown: true,
          headerStyle: {
            backgroundColor: colors.primary,
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      />

      <Stack.Screen
        name="PDF"
        component={PDF}
        options={({route}) => {
          const title = route.params.patientName;

          return {
            title,
            headerShown: true,
            headerStyle: {
              backgroundColor: colors.primary,
            },
            headerTintColor: '#fff',
            headerTitleStyle: {
              fontWeight: 'bold',
            },
          };
        }}
      />

      <Stack.Screen
        name="ApproveTransfer"
        component={ApproveTransfer}
        options={{
          title: 'Aprovar Transferência',
          headerShown: true,
          headerStyle: {
            backgroundColor: colors.primary,
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      />
    </Stack.Navigator>
  );
}

const resetStackWhenTabPress = ({navigation}: {navigation: any}) => ({
  tabPress: (e: any) => {
    const state = navigation.getState();

    if (state) {
      // Grab all the tabs that are NOT the one we just pressed
      const nonTargetTabs = state.routes.filter((r: any) => r.key !== e.target);

      nonTargetTabs.forEach((tab: any) => {
        const stackKey = tab?.state?.key;

        if (stackKey) {
          // Pass the stack key that we want to reset and use popToTop to reset it
          navigation.dispatch({
            ...StackActions.popToTop(),
            target: stackKey,
          });
        }
      });
    }
  },
});

function InProgressRoutes() {
  return (
    <Stack.Navigator
      screenOptions={() => ({
        headerShown: false,
      })}>
      <Stack.Screen
        name="InProgress"
        component={InProgress}
        options={{
          title: 'Transferências em trânsito',
          headerShown: true,
          headerStyle: {
            backgroundColor: colors.primary,
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      />

      <Stack.Screen
        name="Transfer"
        component={Transfer}
        options={{
          title: 'Status da transferência',
          headerShown: true,
          headerStyle: {
            backgroundColor: colors.primary,
          },
          headerTintColor: '#fff',
          headerTitleStyle: {
            fontWeight: 'bold',
          },
        }}
      />
    </Stack.Navigator>
  );
}

function DoneRoutes() {
  return (
    <Stack.Navigator
      screenOptions={() => ({
        headerShown: false,
      })}>
      <Stack.Screen name="Done" component={Done} />
    </Stack.Navigator>
  );
}

export const checkedIcon = ({focused}: {focused: boolean}) => {
  return (
    <View style={styles.iconContainer}>
      <Icon
        name="check-circle-outline"
        color={focused ? colors.secondary : colors.white}
        size={30}
      />
      <Text
        style={{
          ...styles.iconText,
          color: focused ? colors.secondary : colors.white,
        }}>
        Concluídas
      </Text>
    </View>
  );
};

const homeIcon = () => {
  return (
    <View style={styles.iconContainer}>
      <Icon SVG={HomeIcon} size={60} />
    </View>
  );
};

export const ambulanceIcon = ({focused}: {focused: boolean}) => {
  return (
    <View style={styles.iconContainer}>
      <Icon
        name="ambulance"
        color={focused ? colors.secondary : colors.white}
        size={30}
      />
      <Text
        style={{
          ...styles.iconText,
          color: focused ? colors.secondary : colors.white,
        }}>
        Em andamento
      </Text>
    </View>
  );
};

const TabBarComponent = (props: BottomTabBarProps) => {
  const states = props.state;

  return (
    <SafeAreaView style={styles.tabBarContainer}>
      <ImageBackground source={menuBackground} style={styles.tabBarImage}>
        <CustomTabButton
          onPress={() => props.navigation.navigate('DoneRoutes')}>
          {checkedIcon({focused: states.index === 0})}
        </CustomTabButton>
        <CustomTabButton
          absolute
          onPress={() => props.navigation.navigate('HomeRoutes')}>
          {homeIcon()}
        </CustomTabButton>
        <CustomTabButton
          onPress={() => props.navigation.navigate('InProgressRoutes')}>
          {ambulanceIcon({focused: states.index === 2})}
        </CustomTabButton>
      </ImageBackground>
    </SafeAreaView>
  );
};

export default function AppRoutes() {
  return (
    <NavigationContainer>
      <Tab.Navigator
        initialRouteName="HomeRoutes"
        screenListeners={resetStackWhenTabPress}
        tabBar={TabBarComponent}
        screenOptions={() => ({
          lazy: true,
          tabBarStyle: {
            backgroundColor: 'transparent',
            position: 'absolute',
            height: 95,
          },
          headerShown: false,

          // unmountOnBlur: true,
        })}>
        <Tab.Screen
          name="DoneRoutes"
          component={InProgressRoutes}
          options={{
            title: 'Transferências concluídas',
            headerStyle: {
              backgroundColor: colors.primary,
            },
            headerTintColor: '#fff',
            headerTitleStyle: {
              fontWeight: 'bold',
            },
            tabBarIcon: checkedIcon,

            tabBarLabel: () => undefined,
          }}
        />

        <Tab.Screen
          name="HomeRoutes"
          component={HomeRoutes}
          options={{
            headerStyle: {
              backgroundColor: colors.primary,
            },
            headerTintColor: '#fff',
            headerTitleStyle: {
              fontWeight: 'bold',
            },
            tabBarIcon: homeIcon,
            tabBarLabel: () => undefined,
          }}
        />

        <Tab.Screen
          name="InProgressRoutes"
          component={InProgressRoutes}
          options={{
            title: 'Transferências em andamento',
            headerStyle: {
              backgroundColor: colors.primary,
            },
            headerTintColor: '#fff',
            headerTitleStyle: {
              fontWeight: 'bold',
            },
            tabBarIcon: ambulanceIcon,

            tabBarLabel: () => undefined,
          }}
        />
      </Tab.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  customTabButtonButton: {
    justifyContent: 'center',
    alignItems: 'center',
    width: 100,
  },

  customTabButtonContainer: {
    width: 90,
    height: 90,
  },

  iconContainer: {
    alignItems: 'center',
    justifyContent: 'center',
  },

  iconText: {
    fontSize: 12,
  },

  tabBarContainer: {
    position: 'absolute',
    width: '100%',
    height: 70,
    bottom: 0,
  },

  tabBarImage: {
    position: 'absolute',
    width: '100%',
    height: 70,
    resizeMode: 'center',
    flexDirection: 'row',
    justifyContent: 'space-around',
  },
});
