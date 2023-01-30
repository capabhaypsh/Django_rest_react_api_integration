// Need to use the React-specific entry point to import createApi
import { createApi, fetchBaseQuery } from '@reduxjs/toolkit/query/react'
// import type { Pokemon } from './types'

// Define a service using a base URL and expected endpoints
export const candidateProfileApi = createApi({
  reducerPath: 'candidateProfileApi',
  baseQuery: fetchBaseQuery({ baseUrl: 'http://127.0.0.1:8000/api' }),
  endpoints: (builder) => ({
    saveProfile: builder.mutation({
      query: (candidate) => {
        return {
            url:'resume/',
            method:'POST',
            body:'candidate'
        }
      }
    }),
  }),
})

// Export hooks for usage in functional components, which are
// auto-generated based on the defined endpoints
export const { useSaveProfileMutation } = candidateProfileApi
