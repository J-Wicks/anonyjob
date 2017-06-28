import React from 'react';
import { Link } from 'react-router';

export default function Home (props) {

	return(
		<div>
		<p>Add a Job Posting Here</p>
		<form>
			Job Title
			<input type='text' />
			Job Description
			<textarea></textarea>
			Education Field
			<select>
			<option> cool option </option>
			</select>
			Education Level
			<select>
			<option> cool option </option>
			</select>
			Experience Field
			<select>
			<option> cool option </option>
			</select>
			Experience Level
			<select>
			<option> cool option </option>
			</select>
								   	<button className="btn btn-default login-btn" type="submit">Submit</button>
		</form>
		</div>
		)
}