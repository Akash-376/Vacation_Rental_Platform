import { createWebHistory, createRouter } from 'vue-router'
import HostComp from './components/Host.vue'
import LoginComp from './components/Login.vue'
import AddPropertyComp from './components/AddProperty.vue'
import PropertyComp from './components/Properties.vue'
import LogoutComp from './components/Logout.vue'
import RegisterGuestComp from './components/guestRegistration.vue'
import BookingComp from './components/MyBookings.vue'
import MyPropertyComp from './components/MyProperties.vue'

const routes = [
    {
        name:'Host',
        path: '/registerhost',
        component: HostComp
    },
    {
        name:'Login',
        path: '/login',
        component: LoginComp
    },
    {
        name:'AddProperty',
        path: '/addProperty',
        component: AddPropertyComp
    },
    {
        name:'Property',
        path: '/',
        component: PropertyComp
    },
    {
        name:'Logout',
        path: '/logout',
        component: LogoutComp
    },
    {
        name:'registerGuest',
        path: '/registerguest',
        component: RegisterGuestComp
    },
    {
        name:'MyBooking',
        path: '/guests/mybooking',
        component: BookingComp
    },
    {
        name:'MyPropertyComp',
        path: '/hosts/myProperties',
        component: MyPropertyComp
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router