import React, { Component } from 'react'

class ClassCounter extends Component {
  constructor(props) {
    super(props)

    this.state = {
      count: 0,
      firstName: '',
      lastName: ''
    }
  }

  resetCount = () => {
    this.setState({
      count: 0
    })
  }

  incrementCount = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  decrementCount = () => {
    this.setState({
      count: this.state.count - 1
    })
  }

  incrementCount5 = () => {
    this.setState({
      count: this.state.count + 5
    })
  }

  setFirstName = (value) => {
    this.setState({
      firstName: value
    })
  }

  setLastName = (value) => {
    this.setState({
      lastName: value
    })
  }

  render() {
    return (
      <div>
        Class Count: {this.state.count}
        <button onClick={this.resetCount}>Reset</button>
        <button onClick={this.incrementCount}>Increment</button>
        <button onClick={this.decrementCount}>Decrement</button>
        <button onClick={this.incrementCount5}>Increment 5</button>

        <form>
          <input
            type='text'
            value={this.state.firstName}
            onChange={e => this.setFirstName(e.target.value)}
          />
          <input
            type='text'
            value={this.state.lastName}
            onChange={e => this.setLastName(e.target.value)}
          />
          <p>
            Class first name: {this.state.firstName}<br/>
            Class last name: {this.state.lastName}
          </p>
        </form>
      </div>
    )
  }
}

export default ClassCounter
