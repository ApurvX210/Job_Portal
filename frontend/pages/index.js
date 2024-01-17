import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import Layout from '@/components/layout/Layout'
import Home from '@/components/Home'
import axios from 'axios'
const inter = Inter({ subsets: ['latin'] })

export async function getServerSideProps({query}){
  const keyword=query.keyword
  const location=query.location
  
  const res = await axios.get(`${process.env.API_URL}/api/jobs/`)
  const data=res.data
  console.log(data)
  return{
    props:{
      data,
    }
  }
}

export default function Index({data}) {
  return (
    <Layout>
      <Home data={data}/>
    </Layout>
  )
}
