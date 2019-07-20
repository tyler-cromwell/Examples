import React, { Component } from 'react'

class ClassCounter extends Component {
  constructor(props) {
    super(props)
    this.state = {
      count: 0
    }
  }

  componentDidMount() {
    document.title = `Class 02: clicked ${this.state.count} times`
  }

  componentDidUpdate() {
    document.title = `Class 02: clicked ${this.state.count} times`
  }

  incrementCount = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  render() {
    return (
      <div>
        Class Count: {this.state.count}
        <button onClick={this.incrementCount}>Increment</button>
      </div>
    )
  }
}

export default ClassCounter
