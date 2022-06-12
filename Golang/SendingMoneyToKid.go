package main

import "fmt"

type Money struct {
	amount int
	year   int
}

func sendMoney(parent chan Money) {
	for i := 2010; i <= 2022; i++ {
		parent <- Money{1000, i}
	}
	close(parent)
}

func main() {
	money := make(chan Money)

	go sendMoney(money)

	for kidMoney := range money {
		fmt.Printf("Money received by kid in year %d : %d\n", kidMoney.year, kidMoney.amount)
	}
}

/*
Money received by kid in year 2010 : 1000
Money received by kid in year 2011 : 1000
Money received by kid in year 2012 : 1000
Money received by kid in year 2013 : 1000
Money received by kid in year 2014 : 1000
Money received by kid in year 2015 : 1000
Money received by kid in year 2016 : 1000
Money received by kid in year 2017 : 1000
Money received by kid in year 2018 : 1000
Money received by kid in year 2019 : 1000
Money received by kid in year 2020 : 1000
Money received by kid in year 2021 : 1000
Money received by kid in year 2022 : 1000
*/
