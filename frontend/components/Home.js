import React from 'react'
import JobItem from './job/JobItem'
import Link from 'next/link'
import Pagination from 'react-js-pagination'
import { useRouter } from 'next/router'
import Filters from './layout/Filters'
const Home = ({data}) => {
  const{jobs,count,jobPerPage,keyword}=data
  const router=useRouter()
  let {page=1}=router.query
  let queryParams;
  page=Number(page)
  if(typeof window !=='undefined'){
    queryParams=new URLSearchParams(window.location.search);
  }
  const handlePageClick=async(currentPage)=>{
    if(queryParams.has('page')){
      queryParams.set('page',currentPage)
    }else{
      queryParams.append('page',currentPage)
    }
    router.push({
      search:queryParams.toString()
    })
  }
  return (
    <div className="container container-fluid">
      <div className="row">
        <div className="col-xl-3 col-lg-4"><Filters/></div>

        <div className="col-xl-9 col-lg-8 content-left-offset">
          <div className="my-5">
            <h4 className="page-title">{keyword?.length>0 ? `${jobs.length} Result for ${keyword}`:'Latest Jobs'}</h4>
            <Link href="/stats">
              <button className="btn btn-secondary float-right stats_btn">
                Get Topic stats
              </button>
            </Link>
            <div className="d-block">
              <Link href="/search">Go to Search</Link>
            </div>
          </div>
          {jobs && jobs.map((job)=>{
            return <JobItem key={job.id} job={job}/>
          })}
          {jobPerPage<count && (
            <Pagination activePage={page} itemsCountPerPage={jobPerPage} totalItemsCount={count} onChange={handlePageClick} nextPageText={"Next"} prevPageText={"Prev"} firstPageText={"First"} lastPageText={"Last"} itemClass='page-item' linkClass='page-link'/>
          )}
        </div>
      </div>
    </div>
  )
}

export default Home
