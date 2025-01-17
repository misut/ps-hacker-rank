use std::cell::RefCell;
use std::collections::HashSet;
use std::env;
use std::fs::File;
use std::io::{self, BufRead, Write};
use std::rc::{Rc, Weak};

struct Node {
    value: i32,
    next: Option<Rc<RefCell<Node>>>,
}

impl Node {
    fn new(value: i32) -> Rc<RefCell<Self>> {
        Rc::new(RefCell::new(Self { value, next: None }))
    }
}

struct List {
    pub head: Option<Rc<RefCell<Node>>>,
    pub tail: Option<Weak<RefCell<Node>>>,
}

impl List {
    fn new() -> Self {
        List {
            head: None,
            tail: None,
        }
    }

    fn add(&mut self, value: i32) {
        let new_node = Node::new(value);
        match self.tail.take() {
            Some(weak_tail) => {
                if let Some(tail) = weak_tail.upgrade() {
                    tail.borrow_mut().next = Some(new_node.clone());
                }
            }
            None => {
                self.head = Some(new_node.clone());
            }
        }
        self.tail = Some(Rc::downgrade(&new_node));
    }
}

fn cycle(head: Rc<RefCell<Node>>, visited: &mut HashSet<usize>) -> i32 {
    let ptr = Rc::as_ptr(&head) as usize;
    if visited.contains(&ptr) {
        1
    } else {
        visited.insert(ptr);
        match &head.borrow().next {
            Some(next) => cycle(next.clone(), visited),
            None => 0,
        }
    }
}

fn has_cycle(head: Option<Rc<RefCell<Node>>>) -> i32 {
    match head {
        Some(node) => cycle(node, &mut HashSet::new()),
        None => 0,
    }
}

fn main() {
    let stdin = io::stdin();
    let mut stdin_iterator = stdin.lock().lines();

    let mut fptr = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();

    let mut tests = stdin_iterator
        .next()
        .unwrap()
        .unwrap()
        .trim()
        .parse::<i32>()
        .unwrap();

    for _ in 0..tests {
        let index = stdin_iterator
            .next()
            .unwrap()
            .unwrap()
            .trim()
            .parse::<i32>()
            .unwrap();
        let llist_count = stdin_iterator
            .next()
            .unwrap()
            .unwrap()
            .trim()
            .parse::<i32>()
            .unwrap();
        let mut extra: Option<Rc<RefCell<Node>>> = None;
        let mut llist = List::new();
        for i in 0..llist_count {
            let llist_item = stdin_iterator
                .next()
                .unwrap()
                .unwrap()
                .trim()
                .parse::<i32>()
                .unwrap();
            llist.add(llist_item);

            if i == index {
                extra = llist
                    .tail
                    .as_ref()
                    .and_then(|weak_tail| weak_tail.upgrade());
            }
        }
        if let Some(extra_node) = extra {
            if let Some(tail) = &llist.tail {
                if let Some(last_node) = tail.upgrade() {
                    last_node.borrow_mut().next = Some(extra_node);
                }
            }
        }

        let result = has_cycle(llist.head);

        writeln!(&mut fptr, "{}", result).ok();
    }
}
