import Head from 'next/head'
import Script from 'next/script'
import React from 'react'
import Footer from './Footer'
import Header from './Header'
import Link from 'next/link'
const Layout = ({ children,title = 'Jobee - Find your Job Now' }) => {
    return (
        <div>
            <Head>
                <title>{title} - Jobee</title>
                


                <Script
                    strategy="beforeInteractive"
                    src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
                ></Script>

                <Script
                    src="https://kit.fontawesome.com/9edb65c86a.js"
                    crossOrigin="anonymous"
                ></Script>

                <Script
                    strategy="beforeInteractive"
                    src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
                ></Script>

                <Script
                    strategy="beforeInteractive"
                    src="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/js/bootstrap.min.js"
                ></Script>
                <Link rel="stylesheet" href="path/to/font-awesome/css/font-awesome.min.css"></Link>
            </Head>
            <Header/>
            {children}
            <Footer/>
        </div>
    )
}

export default Layout
