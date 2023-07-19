import { createWebHistory, createRouter } from 'vue-router'
import HostComp from './components/Host.vue'
import LoginComp from './components/Login.vue'
import AddPropertyComp from './components/AddProperty.vue'
import PropertyComp from './components/Properties.vue'
import LogoutComp from './components/Logout.vue'

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
    }
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router