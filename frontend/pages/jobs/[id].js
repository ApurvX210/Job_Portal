import JobDetail from '@/components/job/JobDetail'
import Layout from '@/components/layout/Layout'
import NotFound from '@/components/layout/NotFound'
import axios from 'axios'
import React from 'react'

export async function getServerSideProps({ params }) {
  try {
    const { data } = await axios.get(`${process.env.API_URL}/api/jobs/${params.id}/`)
    console.log(data)
    return {
      props: {
        'job': data.job,
        'candidates': data.candidates
      }
    }
  } catch (error) {
    return {
      props: {
        'error': error.response.data.detail
      }
    }
  }

}
const jobDetail = ({ job, candidates,error }) => {
  console.log(error)
  if(error==="Not found."){
    return <NotFound/>
  }
  return (
    <Layout title={job.title}>
      <JobDetail job={job} candidates={candidates} />
    </Layout>
  )
}

export default jobDetail
