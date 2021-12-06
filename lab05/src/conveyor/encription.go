package conveyor

import (
	"strings"
	"time"

	"github.com/brianvoe/gofakeit"
)

type Cipher struct {
	wordsNum int

	Msg string

	flagMsg      bool
	flagReplace  bool
	flagVegenere bool

	startMsg time.Time
	endMsg   time.Time

	startReplace time.Time
	endReplace   time.Time

	startVegenere time.Time
	endVegenere   time.Time
}

func (c *Cipher) SetWordsNum(num int) {
	c.wordsNum = num
}

func GenerateMsg(msg *Cipher) {
	msg.Msg = gofakeit.Sentence(msg.wordsNum)
	msg.Msg = strings.TrimRight(strings.ToLower(msg.Msg), ".")
}

func reverseString(str string) (res string) {
	for _, ch := range str {
		res = string(ch) + res
	}

	return res
}

func ReverseWords(msg *Cipher) {
	words := strings.Fields(msg.Msg)

	for i, word := range words {
		words[i] = reverseString(word)
	}

	msg.Msg = strings.Join(words, " ")
}

func CodeByVegenere(msg *Cipher) {
	key := []rune(gofakeit.Word())
	keyInd := 0
	res := ""

	for _, ch := range msg.Msg {
		if ch >= 'a' && ch <= 'z' {
			ch -= 'a'
			keyCh := key[keyInd] - 'a'

			ch = (ch+keyCh)%26 + 'a'

			keyInd++
			keyInd %= len(key)
		}

		res += string(ch)
	}

	msg.Msg = res
}
