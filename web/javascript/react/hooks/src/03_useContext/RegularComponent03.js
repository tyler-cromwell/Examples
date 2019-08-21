import React from 'react'

import { UserContext, ChannelContext } from '../App'

function RegularComponent03() {
  return (
    <UserContext.Consumer>
      {
        user => {
          return (
            <ChannelContext.Consumer>
              {
                channel => {
                  return <div>User context: {user}, channel context: {channel}</div>
                }
              }
            </ChannelContext.Consumer>
          )
        }
      }
    </UserContext.Consumer>
  )
}

export default RegularComponent03
