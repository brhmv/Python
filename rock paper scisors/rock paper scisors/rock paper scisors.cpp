#include <iostream>
#include<time.h>
using namespace std;



void bot(int botchoice) {

	switch (botchoice)
	{
	case 1:
		cout << "rock ";
		break;
	case 2:
		cout << "paper ";
		break;
	case 3:
		cout << "scissors";
		break;
	default:
		break;
	}
}


int main() {
	srand(time(0));


	int totalscore = 0, userscore = 0, botscore = 0, userchoice = 0, botchoice = 0, lastchoice = 0;

	cout << "Hello :) \n\n ";

	while (totalscore < 5) {
		cout  << "1)rock \n 2)paper \n 3)scissors" << endl;
		cin >> userchoice;

		botchoice = rand() % 3;

		if (botchoice == userchoice) {
			cout << "Bot choosed :";
			bot(botchoice);
			cout << "You choosed : ";
			bot(userchoice);
			cout << "draw :)" << endl;
			cout << "Bot score: " << botscore << " " << "Your score: " << userscore << endl;
		}
		else if (botchoice == 1 && userchoice == 2) {
			cout << "\nBot choosed :";
			bot(botchoice);
			cout << "\nYou choosed : ";
			bot(userchoice);
			cout << "\nYou won :)" << endl;
			userscore++;
			totalscore++;
			cout << "Bot score: " << botscore << " " << "Your score: " << userscore << endl;
		}
		else if (botchoice == 1 && userchoice == 3) {
			cout << "\nBot choosed :";
			bot(botchoice);
			cout << "\nYou choosed : ";
			bot(userchoice);
			cout << "\nBot won :)" << endl;
			botscore++;
			totalscore++;
			cout << "Bot score: " << botscore << " " << "Your score: " << userscore << endl;
		}
		else if (botchoice == 2 && userchoice == 1) {
			cout << "\nBot choosed :";
			bot(botchoice);
			cout << "\nYou choosed : ";
			bot(userchoice);
			cout << "\nBot won :)" << endl;
			botscore++;
			totalscore++;
			cout << "\nBot score: " << botscore << " " << "Your score: " << userscore << endl;
		}
		else if (botchoice == 2 && userchoice == 3) {
			cout << "\nBot choosed :";
			bot(botchoice);
			cout << "\nYou choosed : ";
			bot(userchoice);
			cout << "\nYou won :)" << endl;
			userscore++;
			totalscore++;
			cout << "\nBot score: " << botscore << " " << "Your score: " << userscore << endl;
		}
		else if (botchoice == 3 && userchoice == 1) {
			cout << "\nBot choosed :";
			bot(botchoice);
			cout << "\nYou choosed : ";
			bot(userchoice);
			cout << "\nYou won :)" << endl;
			userscore++;
			totalscore++;
			cout << "\nBot score: " << botscore << " " << "Your score: " << userscore << endl;
		}
		else if (botchoice == 3 && userchoice == 2) {
			cout << "\nBot choosed :";
			bot(botchoice);
			cout << "\nYou choosed : ";
			bot(userchoice);
			cout << "\nBot won :)" << endl;
			botscore++;
			totalscore++;
			cout << "\nBot score: " << botscore << " " << "Your score: " << userscore << endl;
		}

		if (botscore == 3) {
			cout << "\nBot won :)" << endl;
			cout << "Bot's score: " << botscore << " " << "Your score: " << userscore << endl;


		}
		else if (userscore == 3) {
			cout << "You won :)" << endl;
			cout << "Bot's score: " << botscore << " " << "Your score: " << userscore << endl;
		}


		//cout << "Do you want to play again ? \n 1)Yes \n 2)No " << endl;
		//cin >> lastchoice;

		/*
		if (totalscore > 5) {
			if (lastchoice == 1) {
				totalscore = 0;
				cout << "a";
			}
			else if (lastchoice == 2) {
				cout << "Thanks for playing :)" << endl;
				break;
			}
			else {
				cout << "Choose one of twol choices";
			}
		}*/
	}

}
























