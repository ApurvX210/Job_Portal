import Head from 'next/head'
import Image from 'next/image'
import { Inter } from 'next/font/google'
import styles from '@/styles/Home.module.css'
import Layout from '@/components/layout/Layout'
import Home from '@/components/Home'
import axios from 'axios'
const inter = Inter({ subsets: ['latin'] })

export async function getServerSideProps({query}){
  const keyword=query.keyword || ''
  const location=query.location || ''
  const page=query.page || '1'
  const jobType=query.jobType || ''
  const education=query.education || ''
  const experience=query.experience || ''
  let min_salary = "";
  let max_salary = "";

  if (query.salary) {
    const [min, max] = query.salary.split("-");
    min_salary = min;
    max_salary = max;
  }
  const queryString=`keyword=${keyword}&location=${location}&page=${page}&jobType=${jobType}&education=${education}&experience=${experience}&min_salary=${min_salary}&max_salary=${max_salary}`
  const res = await axios.get(`${process.env.API_URL}/api/jobs?${queryString}`)
  const data=res.data
  data.keyword=keyword
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
