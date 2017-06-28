import React, { Component } from 'react';
import axios from 'axios';
import { hashHistory } from 'react-router';
import NewPosting from '../components/NewPosting';
// import AllProducts from '../components/AllProducts';
import {connect} from 'react-redux';
import { logoutUser, receiveProducts} from '../action-creators'


class EmployerDashboardContainer extends Component {

  constructor(props){
    super(props);
    this.state = {
      jobTitle: '',
      jobDescription: '',
      educationField: '',
      educationLevel: '',
      experienceField: '',
      experienceLevel: '',
   };
	this.handleJobTitle = this.handleJobTitle.bind(this);
	this.handleJobDescription = this.handleJobDescription.bind(this);
	this.handleEducationField = this.handleEducationField.bind(this);
	this.handleEducationLevel = this.handleEducationLevel.bind(this);
	this.handleExperienceField = this.handleExperienceField.bind(this);
	this.handleExperienceLevel = this.handleExperienceLevel.bind(this);
  }

	handleJobTitle (event) {
		const value = event.target.value;
		this.setState({
			jobTitle: value
		})
	}

	handleJobDescription (event) {
		const value = event.target.value;
		this.setState({
			jobDescription: value
		})
	}

	handleEducationField (event) {
		const value = event.target.value;
		this.setState({
			educationField: value
		})
	}

	handleEducationLevel (event) {
		const value = event.target.value;
		this.setState({
			educationLevel: value
		})
	}
	handleExperienceField (event) {
		const value = event.target.value;
		this.setState({
			experienceField: value
		})
	}
	handleExperienceLevel (event) {
		const value = event.target.value;
		this.setState({
			experienceLevel: value
		})
	}

  render () {
    return (
      <div id="entire-container">
      <NewPosting 
      handleJobTitle={this.handleJobTitle}
      handleJobDescription={this.handleJobDescription}
      handleEducationField={this.handleEducationField}
      handleEducationLevel={this.handleEducationLevel}
	  handleExperienceField={this.handleExperienceField}
	  handleExperienceLevel={this.handleExperienceLevel}
      />
      </div>
    )
  }
}

const mapStateToProps = function(state){
  return {
    props: 'props'
  }
}

export default connect(mapStateToProps)(EmployerDashboardContainer)