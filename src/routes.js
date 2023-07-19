import { createWebHistory, createRouter } from 'vue-router'
import HostComp from './components/Host.vue'
import LoginComp from './components/Login.vue'


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
    
]

const router = createRouter({
    history:createWebHistory(),
    routes
})

export default router