class Coordinator:
    def __init__(self) -> None:
        self.participants = []
        self.vote = []
    def register_participant(self,participant):
        self.participants.append(participant)
    def send_prepare(self):
        print('\n-------------PREPARE PHASE-------------')
        for part in self.participants:
            part.receive_prepare()
    def start_voting(self):
        print('\n-------------VOTING PHASE-------------')
        for part in self.participants:
            self.vote.append(part.send_voting())
    def send_commit(self):
        print("\n-------------INDIVIDUAL LOGS-------------")
        for part in self.participants:
            part.receive_commit()
    def make_decision(self):
        print("\n-------------DESCISION PHASE-------------")
        if 0 in self.vote:
            print('Transaction Aborted as all the Participant sites are not ready')
        else:
            print('Transaction Committed successfully as all the Participant sites were ready')

class Participants:
    def __init__(self,name) -> None:
        self.name = name
        self.prepared = False
    def receive_prepare(self):
        print(f'{self.name} is in prepare phase.')
    def send_voting(self):
        val = int(input(f'Enter 1 if {self.name} is ready to commit 0 if {self.name} is not ready to commit:\n'))
        if val:
            self.prepared = True
        return val
    def receive_commit(self):
        if self.prepared:
            print(f'{self.name} committed the transaction.')
        else:
            print(f'{self.name} cannot commit. Not prepared')


try:
    num_participants = int(input('Enter the number of participants: '))
    coordinator = Coordinator()
    for i in range(num_participants):
        participant = Participants(input(f'Enter the participant{i+1} name: '))
        coordinator.register_participant(participant)
    coordinator.send_prepare()
    coordinator.start_voting()
    coordinator.send_commit()
    coordinator.make_decision()
    print('Transaction Completed!')
except:
    print('\n\nTransaction Aborted due to Error Interrupt')
