import { useState } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import Col from 'react-bootstrap/Col';
import Modal from 'react-bootstrap/Modal';

const BlogPreview = ({ blog, handleDelete }) => {
    const [modalShow, setModalShow] = useState(false)

    return (
        <Col xs={6}>
            <Card className='blog-preview'>
                <Card.Header>{ blog.title }</Card.Header>
                <Card.Body>
                    <Card.Text>Written by {blog.author}</Card.Text>
                    <Button variant="outline-danger" onClick={() => setModalShow(true)}>Delete blog</Button>
                </Card.Body>
            </Card>

            <Modal show={ modalShow } centered>
                <Modal.Header>
                    <Modal.Title>Delete blog</Modal.Title>
                </Modal.Header>

                <Modal.Body>
                    <p>¿Are you sure to delete { blog.title }?</p>
                </Modal.Body>

                <Modal.Footer>
                    <Button variant="secondary" onClick={() => setModalShow(false)}>Cancel</Button>
                    <Button variant="danger" onClick={() => handleDelete(blog.id)}>Delete</Button>
                </Modal.Footer>
            </Modal>
        </Col>
    );
}
 
export default BlogPreview;