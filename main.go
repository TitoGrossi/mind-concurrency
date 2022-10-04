package main

import (
	"fmt"
	"math/rand"
	"time"
)

func main() {
	c := make(chan int)

	go retrieveData(c)

	done := make(chan bool)
	go complexComputation(c, done)

	// semaphore
	<-done
}

func complexComputation(c chan int, done chan bool) {
	// esperando até a mensagem do canal chegar, rotina parada até então
	variable := <-c
	// simulação de uma espera de uma operação que demora muito tempo, talvez processando um array muito grande
	// com um algoritmo O(n^4)
	time.Sleep(time.Millisecond * 1000)
	fmt.Println(variable + 1)
	done <- true
}

func retrieveData(c chan int) {
	// simulação de uma espera de I/O
	time.Sleep(time.Millisecond * 1000)
	c <- rand.Int()
}
