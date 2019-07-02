import React, { Component } from 'react'

class ClassCounter extends Component {
  constructor(props) {
    super(props)

    this.state = {
      count: 0
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

  render() {
    return (
      <div>
        Class Count: {this.state.count}
        <button onClick={this.resetCount}>Reset</button>
        <button onClick={this.incrementCount}>Increment</button>
        <button onClick={this.decrementCount}>Decrement</button>
        <button onClick={this.incrementCount5}>Increment 5</button>
      </div>
    )
  }
}

export default ClassCounter
