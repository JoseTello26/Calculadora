pipeline {
    agent any
    stages {
        stage('Exec') {
            steps {
                sh "python3 calculadora.py 3 2"
            }
        }
	stage('Unit test'){
	    steps{
		sh "python3 -m unittest -v test_calculadora.py"
	    }
	}
    }
}
